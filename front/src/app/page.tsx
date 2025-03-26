'use client'

import { useLayoutEffect, useRef } from "react";
import * as am5 from "@amcharts/amcharts5";
import * as am5map from "@amcharts/amcharts5/map";
import am5geodata_brazil from "@amcharts/amcharts5-geodata/brazilLow";

export default function Home() {
  const chartRef = useRef(null);

  useLayoutEffect(() => {
    if (!chartRef) return;
    const root = am5.Root.new(chartRef.current!);

    const chart = root.container.children.push(
      am5map.MapChart.new(root, {
        projection: am5map.geoMercator(),
        panX: "rotateX"
      })
    );

    // Cria uma série de polígonos baseada no geodata do Brasil
    const polygonSeries = chart.series.push(
      am5map.MapPolygonSeries.new(root, {
        geoJSON: am5geodata_brazil,
        // Se desejar, pode excluir outras regiões
        exclude: ["BR-DF"]
      })
    );

    polygonSeries.events.once("datavalidated", () => {
      const rioItem = polygonSeries.getDataItemById("BR-RJ");
      if (rioItem) {
        const mapPolygon = rioItem.get("mapPolygon");
        if (mapPolygon) {
          const centroid = mapPolygon.geoCentroid();
          chart.zoomToGeoPoint(centroid, 5, true);
        }
      }
    });

    return () => {
      root.dispose();
    };
  }, []);

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <div ref={chartRef} className="w-100 h-60"></div>
        <div className="w-45">
          <h3>Lista</h3>
        </div>
      </main>
    </div>
  );
}
