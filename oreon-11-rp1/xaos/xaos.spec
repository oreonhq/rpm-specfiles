%global source0_hash 4bb1c6bdc3a136e7bdceaa626ae48944ef289cdc092dc5e46b4f8e9e049c5b07
Name:           xaos
Version:        4.3.4
Release:        1%{?dist}
Summary:        A fast, portable real-time interactive fractal zoomer
%global forgeurl https://github.com/xaos-project/XaoS
%global tag release-%{version}
%forgemeta
License:        GPL-2.0-or-later
URL:            %forgeurl
Source0:        %{forgeurl}/archive/%{tag}/XaoS-%{tag}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake(qt6)
BuildRequires:  gcc
BuildRequires:  libatomic
BuildRequires:  qt6-linguist
# /oreon:deps
%description
XaoS is a fast, portable real-time interactive fractal zoomer. It
displays the Mandelbrot set (among other escape time fractals) and
allows you zoom smoothly into the fractal. Various coloring modes are
provided for both the points inside and outside the selected set. XaoS
supports switching between Julia and Mandelbrot fractal types and
on-the-fly plane switching.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%qmake_qt6
%make_build STRIP=:
%install
install -D --mode 0755 --target-directory %{buildroot}%{_bindir} bin/%{name}
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/XaoS/catalogs catalogs/*.cat
cp --archive examples tutorial %{buildroot}%{_datadir}/XaoS
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/metainfo xdg/%{name}.appdata.xml
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/applications xdg/io.github.xaos_project.XaoS.desktop
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/pixmaps xdg/%{name}.png
install -D --mode 0644 --target-directory %{buildroot}%{_mandir}/man6 doc/%{name}.6
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
