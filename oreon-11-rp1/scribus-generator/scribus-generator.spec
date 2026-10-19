%global source0_hash 8e70e43930dc6e1634d95787dc7d316462461fa1fc00e2ba0836727282cdce8e
Name:		scribus-generator
Version:	4.0
Release:        1%{?dist}
Summary:        Open source high-quality PDF template and mail-merge alternative
License:	MIT
URL:		https://github.com/berteh/ScribusGenerator
Source0:        https://github.com/berteh/ScribusGenerator/archive/%{version}.tar.gz#/ScribusGenerator-%{version}.tar.gz
Source1:	%{name}.metainfo.xml
Requires:	python3-tkinter
Requires:	scribus
BuildArch:	noarch
# oreon:deps
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(python3)
# /oreon:deps
%description
Mail-Merge-like extension to Scribus, to generate Scribus and 
PDF documents automatically from external data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ScribusGenerator-%{version}

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

%build

%install
install -Dpm 0644 *.{py,conf} -t %{buildroot}%{_datadir}/scribus/scripts/
chmod +x %{buildroot}%{_datadir}/scribus/scripts/*.py
cp -r {example,pic} %{buildroot}%{_datadir}/scribus/scripts/
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
