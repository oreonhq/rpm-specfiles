%global source0_hash 66fee83318d0a897edf92d134b07628550265c5046e176a47f49980a5f80fe26
Name:      glglobe
Version:   0.2
Release:        46%{?dist}
Summary:        OpenGl Globe - Earth simulation for linux
License:   GPL-2.0-only
URL:       http://www.geocities.com/harpin_floh/glglobe_page.html
Source0:        http://www.geocities.com/harpin_floh/mysoft/glglobe-0.2.tar.gz
Source1:   glglobe.16x16.png
Source2:   glglobe.24x24.png
Source3:   glglobe.48x48.png
Source4:   glglobe.desktop
Patch0:    glglobe-0.2-fix-newline-warnings.patch
Patch1:    glglobe-0.2-fix-signedness-differs-warnings.patch
Patch2:    glglobe-0.2-set-default-params.patch
Patch3:    glglobe-0.2-makefile_accept_passed_optflags.patch
Patch4:    glglobe-freeglut.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
GLGlobe is an OpenGL - globe simulation for Linux. It was inspired by XGlobe or
XEarth and can use the marker-files of these programs. The simulation includes
day light and night time rendering, and the globe can be rotated and scaled 
interactively, or automatically rotated based on the current time of day

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# -n sets tgz extract folder to match version
%setup -q -n glglobe
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p0

%build

export CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 glglobe %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/glglobe
install -p -m 0644 depths_1440.jpg xglobe-markers earth-markers-schaumann %{buildroot}%{_datadir}/glglobe
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
install -p -m 644 %{SOURCE1} \
        %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/24x24/apps/
install -p -m 644 %{SOURCE2} \
        %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE3} \
        %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications %{SOURCE4}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
