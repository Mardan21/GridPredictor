// import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-12">
      <section className="text-center mb-20">
        <h1 className="text-5xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-red-700 to-red-500">
          RaceCast Pro
        </h1>
        <p className="text-xl mb-8 max-w-3xl mx-auto">
          Advanced F1 analytics platform with real-time predictions, historical
          comparisons, and championship simulations powered by machine learning.
        </p>
        <div className="flex flex-wrap justify-center gap-4">
          <Link href="/dashboard" className="btn-primary">
            Go to Dashboard
          </Link>
          <Link href="/predict" className="btn-secondary">
            Race Predictions
          </Link>
        </div>
      </section>

      <section className="mb-20">
        <h2 className="text-3xl font-bold mb-12 text-center">Key Features</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div className="card p-6">
            <h3 className="text-xl font-bold mb-2 text-center">
              Race Prediction
            </h3>
            <p className="text-gray-600">
              XGBoost-powered predictions for upcoming races with finish
              probabilities and feature explanation.
            </p>
          </div>

          <div className="card p-6">
            <h3 className="text-xl font-bold mb-2 text-center">
              Monte-Carlo Simulation
            </h3>
            <p className="text-gray-600">
              Run 10,000 simulated seasons to forecast championship outcomes and
              explore &quot;what-if&quot; scenarios.
            </p>
          </div>

          <div className="card p-6">
            <h3 className="text-xl font-bold mb-2 text-center">
              Interactive Dashboards
            </h3>
            <p className="text-gray-600">
              Real-time stats, visualizations, and performance trends with
              responsive charts and filters.
            </p>
          </div>

          <div className="card p-6">
            <h3 className="text-xl font-bold mb-2 text-center">
              Historical Comparisons
            </h3>
            <p className="text-gray-600">
              Compare drivers, teams, and seasons across Formula 1 history with
              detailed metrics and visualizations.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
