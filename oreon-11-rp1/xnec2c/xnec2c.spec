%global source0_hash 787fe8346c9bfc2d47b46325ed77bce6be21a5ae547361e0822c1ade49fb9046

Name:           xnec2c
Version:        4.4.16
Release:        7%{?dist}
Summary:        GTK based graphical wrapper for nec2c

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.5b4az.org/
Source0:        https://github.com/KJ7LNW/xnec2c/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source100:      xnec2c.png

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make

Requires:       nec2c%{?_isa}
# For BLAS acceleration.  Really these are suggested, but strongly
# recommended for performance.  xnec2c detects available BLAS
# libraries at runtime:
Recommends: atlas
Recommends: openblas-serial
Recommends: openblas-threads
Recommends: openblas-openmp

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

# Install scalable icon for Fedora
# Note /usr/share/pixmap/xnec2c.svg is needed for the icon to show in el7.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -pm 644 resources/xnec2c.svg \
	%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

desktop-file-install --vendor="" \
  --dir=%{buildroot}%{_datadir}/applications \
  files/%{name}.desktop

# Remove incorrectly installed files by make
rm -rf %{buildroot}%{_docdir}/%{name}/*.1.gz \
       %{buildroot}%{_datadir}/pixmaps

%if 0%{?fedora}
# Appdata
mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2017 Richard Shaw <hobbes1069@gmail.com> -->
<component type="desktop">
  <id>%{name}.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>GPL-2.0+</project_license>
  <name>xnec2c</name>
  <summary>A multi-threaded EM tool based on NEC2 to model antenna radiation patterns.</summary>
  <description>
    <p>
Xnec2c is a high-performance multi-threaded electromagnetic simulation
package to model antenna near- and far-field radiation patterns for
Linux and UNIX operating systems. The original FORTRAN version of NEC2
was ported to C by Neoklis Kyriazis, 5B4AZ and released as nec2c. Later
he wrote xnec2c, a graphical interface for ease of use with many more
features.
    </p>
  </description>
  <categories>
  	<category>Electronics</category>
  	<category>Science</category>
  	<category>Math</category>
  	<category>NumericalAnalysis</category>
  </categories>
  <screenshots>
    <screenshot type="default">
      <image>https://www.xnec2c.org/images/radiation.png</image>
    </screenshot>
  </screenshots>
  <url type="homepage">%{url}</url>
  <content_rating type="oars-1.1"/>
  <update_contact>hobbes1069@gmail.com</update_contact>
</component>
EOF
%endif

%files
%doc AUTHORS ChangeLog README
%doc doc/NearFieldCalcs.txt doc/NEC2-bug.txt doc/nec2c.txt doc/xnec2c.html
%doc doc/images
%doc examples
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/x-nec2.xml
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{?fedora:%{_datadir}/appdata/%{name}.appdata.xml}
%{_mandir}/man1/%{name}.*

%changelog
%autochangelog
