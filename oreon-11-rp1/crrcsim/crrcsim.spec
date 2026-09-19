%global source0_hash abe59b35ebb4322f3c48e6aca57dbf27074282d4928d66c0caa40d7a97391698

Name:          crrcsim
Version:       0.9.13
Release:       27%{?dist}
Summary:       Model-Airplane Flight Simulation Program
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:       GPL-2.0-only
URL:           http://sourceforge.net/apps/mediawiki/crrcsim/
Source0:       http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# upstream report: http://preview.tinyurl.com/bnryakb
Patch0:        %{name}-0.9.13-support-for-platforms-without-sys-io.h.patch
# aarch64 support added
# upstream report: http://preview.tinyurl.com/cass62h
Patch1:        %{name}-0.9.13-aarch64-support-added.patch
# fix for https://bugzilla.redhat.com/show_bug.cgi?id=1307411
# upstream report: https://sourceforge.net/p/crrcsim/bugs/35/
Patch2:        %{name}-0.9.13-gcc-7-fixes.patch
# hg export -r 1554 >crrcsim-0.9.13-issue-41.patch
# fix fof rhbz#1575624
Patch3:        %{name}-0.9.13-issue-41.patch
# Fix compilation with CGAL >5.x
# upstream report: https://sourceforge.net/p/crrcsim/bugs/44/
Patch4:        %{name}-0.9.13-cgal-header-mode-only.patch

# It is only meant for development purposes.
%global build_with_cmake %{?_with_cmake:1}%{!?_with_cmake:0}

%global the_desktop_file packages/Fedora/CRRCsim.desktop
%global the_icon_file %{_datadir}/%{name}/icons/%{name}.png

%if %{build_with_cmake}
BuildRequires: cmake
%endif
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: /usr/bin/git
BuildRequires: portaudio-devel
BuildRequires: SDL-devel
BuildRequires: freeglut-devel
BuildRequires: plib-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: CGAL-devel
BuildRequires: desktop-file-utils
BuildRequires: make

%description
Crrcsim is a model-airplane flight simulation program.
Using it, you can learn how to fly model aircraft, test new aircraft designs,
and improve your skills by practicing on your computer.

The flight model is very realistic.
The flight model parameters are calculated based on a 3D representation
of the aircraft. Stalls are properly modeled as well.
Model control is possible with your own RC transmitter, or any input device
such as joystick, mouse, keyboard.

%package doc
Summary:       Documentation for %{name}
BuildArch:     noarch

%description doc
Documentation for %{name} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git

# Correct EOL.
for i in \
    documentation/input_method/PARALLEL_1_to_3/crrcsim_at90s1200.hex \
    documentation/models/*.txt \
    documentation/Install_Win32.txt \
    documentation/dlportio.txt; do
        sed -i 's#\r##g' $i;
done

# Remove executable permission.
chmod a-x src/mod_landscape/heightdata.h

# Correct file encoding.
for i in documentation/thermals/table*.cpp; do
  iconv -f iso-8859-1 -t utf-8 -o $i{.utf8,} && mv $i{.utf8,}
done

# Desktop file: correct the icon file location.
sed -i 's#^\(Icon.*=\).*#\1%{the_icon_file}#g' %{the_desktop_file}

# Desktop file: correct categories.
# Reported upstream: http://preview.tinyurl.com/cep8rvp
sed -i 's#^\(Categories=\).*#\1Game;Simulation;#g' %{the_desktop_file}

# Desktop file: remove deprecated "Encoding" key.
# Reported upstream: http://preview.tinyurl.com/cep8rvp
sed -i 's#^Encoding=.*##g' %{the_desktop_file}

# Minimal approach to satisfy the linker.
# Reported upstream: http://preview.tinyurl.com/d3cg4s2
sed -i 's#-lboost_thread-mt#-lboost_thread#g' Makefile.in configure

%if %{build_with_cmake}
# Remove reference to not existing file.
sed -i 's#\(.*m44_test.*\)#\#\1#g' src/mod_math/CMakeLists.txt
%endif

%build
%if %{build_with_cmake}
 mkdir -p build
 pushd build
 %cmake ..
 make %{?_smp_mflags}
 popd
%else
 %configure
 make %{?_smp_mflags}
%endif

%install
make DESTDIR=%{buildroot} install
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{the_desktop_file}
rm -f %{buildroot}%{_datadir}/%{name}/icons/%{name}.{ico,xpm}
%find_lang %{name} --with-man

# adding to installed docs in order to avoid using %%doc magic
for f in AUTHORS COPYING HISTORY ; do
    cp -p $f %{buildroot}%{_docdir}/%{name}/${f}
done

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/CRRCsim.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/crrcsim/feature-requests/37/
SentUpstream: 2014-07-11
-->
<application>
  <id type="desktop">CRRCsim.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Charles River RC Flight Simulator</name>
  <summary>Flight simulator for model remote controlled aircraft</summary>
  <description>
    <p>
      The Charles River RC Flight Simulator (CRRCSim) is a flight simulator to
      test fly model aircraft.
      CRRCSim comes with over 15 different types of model gliders and planes, and
      lets you fly in 3 different locations.
    </p>
  </description>
  <url type="homepage">https://sourceforge.net/projects/crrcsim/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/CRRCsim/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/CRRCsim/b.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files -f %{name}.lang
%{_bindir}/crrcsim
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/CRRCsim.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/HISTORY

%files doc
# all documentation in this package (including the license)
%{_docdir}/%{name}/

%changelog
%autochangelog
