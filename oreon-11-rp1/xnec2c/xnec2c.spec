%global source0_hash c4b7eaf4d45242a805b6d697136ad13b1ff751db1d5854d31a755da7f1973045
Name:           xnec2c
Version:        4.4.18
Release:        1%{?dist}
Summary:        GTK based graphical wrapper for nec2c
License:        GPL-2.0-or-later
URL:            http://www.5b4az.org/
Source0:        https://github.com/KJ7LNW/xnec2c/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source100:      xnec2c.png
Requires:       nec2c%{?_isa}
Recommends: atlas
Recommends: openblas-serial
Recommends: openblas-threads
Recommends: openblas-openmp
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Xnec2c is a high-performance multi-threaded electromagnetic simulation
package to model antenna near- and far-field radiation patterns for
Linux and UNIX operating systems. The original FORTRAN version of NEC2
was ported to C by Neoklis Kyriazis, 5B4AZ and released as nec2c. Later
he wrote xnec2c, a graphical interface for ease of use with many more
features:
	Multi-threading operation on SMP machines
	On-demand Calculation
	Built-in NEC2 input file editor
	Accelerated Linear Algebra Support
	Interactive Operation
	User Interface
	Color Coding
	and much more.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

pushd examples
iconv --from=ISO-8859-1 --to=UTF-8 conductivity.txt > conductivity.txt.new && \
touch -r conductivity.txt conductivity.txt.new && \
mv conductivity.txt.new conductivity.txt

%build

autoreconf -fi
%configure
%make_build CFLAGS="%{optflags}"
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -pm 644 %{SOURCE100} \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -pm 644 resources/xnec2c.svg \
	%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
desktop-file-install --vendor="" \
  --dir=%{buildroot}%{_datadir}/applications \
  files/%{name}.desktop
rm -rf %{buildroot}%{_docdir}/%{name}/*.1.gz \
       %{buildroot}%{_datadir}/pixmaps
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
