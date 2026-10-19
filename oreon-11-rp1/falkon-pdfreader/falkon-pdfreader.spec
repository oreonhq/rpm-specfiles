%global source0_hash 83482c8e6b46b89e6babf213be68b19ceaf345e040e94e4431e6900b48d3d56b
%global gitcommit_full dcb8453c21a4562727215e899dad083637bc30d3
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20200924
%global debug_package %{nil}
Name:           falkon-pdfreader
Version:        0
Release:        1%{?dist}
Summary:        PDF reader extension for Falkon using pdf.js
License:        GPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/Tarptaeya/PDFReader
Source0:        https://api.github.com/repositories/1555%{version}844%{version}/tarball/%{gitcommit_full}
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}
Requires:       falkon%{?_isa} >= 3.1.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
%{summary}.

%prep

%autosetup -n tarptaeya-PDFReader-%{gitcommit}
mv pdfreader/pdfjs/LICENSE LICENSE_pdfjs

%build

%cmake_kf5 -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
