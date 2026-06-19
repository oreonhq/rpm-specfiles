%global source0_hash 78c51bcf21b54e58bb6329accbb4dae03b2ed79b520f9a01e734bd9de530953f

Name:           lv2
Version:        1.18.10
Release:        %autorelease
Summary:        Audio Plugin Standard

# lv2specgen template.html is CC-AT-SA
License:        ISC
URL:            https://lv2plug.in
Source0:        https://lv2plug.in/spec/lv2-%{version}.tar.xz
Patch0:         %{name}-no-gtk2.patch

BuildRequires:  asciidoc
BuildRequires:  cairo-devel >= 1.8.10
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libsndfile-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  python3-pygments
BuildRequires:  python3-rdflib
BuildRequires:  python3-markdown
BuildRequires:  python3-lxml

%description
LV2 is a standard for plugins and matching host applications, mainly
targeted at audio processing and generation.  

There are a large number of open source and free software synthesis
packages in use or development at this time. This API ('LV2') attempts
to give programmers the ability to write simple 'plugin' audio
processors in C/C++ and link them dynamically ('plug') into a range of
these packages ('hosts').  It should be possible for any host and any
plugin to communicate completely through this interface.

LV2 is a successor to LADSPA, created to address the limitations of
LADSPA which many hosts have outgrown.

%package        devel
Summary:        API for the LV2 Audio Plugin Standard

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-rdflib
Requires:       python3-markdown

%description    devel
lv2-devel contains the lv2.h header file and headers for all of the
LV2 specification extensions and bundles.

Definitive technical documentation on LV2 plug-ins for both the host
and plug-in is contained within copious comments within the lv2.h
header file.

%package        doc
Summary:        Documentation for the LV2 Audio Plugin Standard
BuildArch:      noarch

%description    doc
Documentation for the LV2 plugin API.

%package        example-plugins
Summary:        Examples of the LV2 Audio Plugin Standard
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    example-plugins
Example plugins for the LV2 Audio Plugin Standard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# Fix wrong interpreter in lv2specgen.py
sed -i '1s|^#!.*|#!%{__python3}|' lv2specgen/lv2specgen.py

%build
%meson \
  -D docs=enabled \
  -D old_headers=true \
  -D tests=disabled

%meson_build

%install
%meson_install

# Let RPM pick docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%files
%license COPYING
%doc NEWS README.md
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/atom.lv2
%{_libdir}/%{name}/buf-size.lv2
%{_libdir}/%{name}/core.lv2
%{_libdir}/%{name}/data-access.lv2
%{_libdir}/%{name}/dynmanifest.lv2
%{_libdir}/%{name}/event.lv2
%{_libdir}/%{name}/instance-access.lv2
%{_libdir}/%{name}/log.lv2
%{_libdir}/%{name}/midi.lv2
%{_libdir}/%{name}/morph.lv2
%{_libdir}/%{name}/options.lv2
%{_libdir}/%{name}/parameters.lv2
%{_libdir}/%{name}/patch.lv2
%{_libdir}/%{name}/port-groups.lv2
%{_libdir}/%{name}/port-props.lv2
%{_libdir}/%{name}/presets.lv2
%{_libdir}/%{name}/resize-port.lv2
%{_libdir}/%{name}/schemas.lv2
%{_libdir}/%{name}/state.lv2
%{_libdir}/%{name}/time.lv2
%{_libdir}/%{name}/ui.lv2
%{_libdir}/%{name}/units.lv2
%{_libdir}/%{name}/uri-map.lv2
%{_libdir}/%{name}/urid.lv2
%{_libdir}/%{name}/worker.lv2

%files devel
%{_bindir}/lv2specgen.py
%{_bindir}/lv2_validate
%{_datadir}/lv2specgen
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/lv2.h

%files example-plugins
%{_libdir}/%{name}/eg-amp.lv2
%{_libdir}/%{name}/eg-fifths.lv2
%{_libdir}/%{name}/eg-metro.lv2
%{_libdir}/%{name}/eg-midigate.lv2
%{_libdir}/%{name}/eg-params.lv2

%files doc
%doc %{_vpath_builddir}/doc/*

%changelog
%autochangelog
