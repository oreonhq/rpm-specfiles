%global source0_hash 9f6f7f00664adcd470069cbe2b05e41bd1e9bbe4506856a8029c56353eacee7d
Name:           pdfarranger
Version:        1.14.0
Release:        1%{?dist}
Summary:        PDF file merging, rearranging, and splitting
License:        GPL-3.0-or-later
URL:            https://github.com/pdfarranger/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExcludeArch:    %{ix86}
Recommends:     python3-img2pdf >= 0.3.4
Requires:       python3-gobject
Requires:       gtk3
Requires:       python3-cairo
Requires:       poppler-glib
Provides:       pdfshuffler = %{version}-%{release}
Obsoletes:      pdfshuffler < 0.6.1-1
%global app_id com.github.jeromerobert.pdfarranger
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pdfarranger = %{version}-%{release}
# /oreon:deps
%description
PDF Arranger is a small python-gtk application, which helps the user to merge 
or split pdf documents and rotate, crop and rearrange their pages using an 
interactive and intuitive graphical interface. It is a frontend for pikepdf.

PDF Arranger is a fork of Konstantinos Poulios’s PDF-Shuffler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%find_lang %{name}
ln -s pdfarranger %{buildroot}%{_bindir}/pdfshuffler
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
python3 -X tracemalloc -u -m unittest -v -f tests.test_core
python3 -X tracemalloc -u -m unittest -v -f tests.test_exporter
%files

%changelog

%autochangelog
