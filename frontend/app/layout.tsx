import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Providers } from "./providers";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export const metadata: Metadata = {
  title: "RaceCast Pro - F1 Analytics Platform",
  description:
    "Predictive analytics platform for Formula 1 racing with machine learning predictions, historical comparisons and race simulations.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${inter.variable} font-sans antialiased h-full bg-gray-50 text-gray-900`}
      >
        <Providers>
          <div className="min-h-screen flex flex-col">
            <header className="bg-white border-b border-gray-200">
              <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between h-16">
                  <div className="flex items-center">
                    <span className="text-[#e10600] font-bold text-xl">
                      RaceCast<span className="text-gray-900">Pro</span>
                    </span>
                  </div>
                </div>
              </div>
            </header>
            <main className="flex-grow">{children}</main>
            <footer className="bg-white border-t border-gray-200 py-8">
              <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <p className="text-center text-gray-500">
                  &copy; {new Date().getFullYear()} RaceCast Pro. All rights
                  reserved.
                </p>
              </div>
            </footer>
          </div>
        </Providers>
      </body>
    </html>
  );
}
