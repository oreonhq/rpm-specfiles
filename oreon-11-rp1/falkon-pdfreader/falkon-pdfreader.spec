%global source0_hash none

%global gitcommit_full dcb8453c21a4562727215e899dad083637bc30d3
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20200924

%global debug_package %{nil}

Name:           falkon-pdfreader
Version:        0
Release:        0.20.%{date}git%{gitcommit}%{?dist}
Summary:        PDF reader extension for Falkon using pdf.js

# Automatically converted from old format: GPLv3+ and ASL 2.0 - review is highly recommended.
License:        GPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/Tarptaeya/PDFReader
Source0:        %{url}/tarball/%{gitcommit_full}

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

Requires:       falkon%{?_isa} >= 3.1.0

%description
%{summary}.

%prep
%autosetup -n Tarptaeya-PDFReader-%{gitcommit}
mv pdfreader/pdfjs/LICENSE LICENSE_pdfjs

%build
%cmake_kf5

%install
%cmake_install

%files
%license LICENSE LICENSE_pdfjs
%doc README.md
%{_kf5_qtplugindir}/falkon/qml/pdfreader

%changelog
%autochangelog
