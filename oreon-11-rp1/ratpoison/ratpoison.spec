%global source0_hash d98fa4be025ecca453c407ff311ab3949f29f20d6d8abedf8f0716b85fc8d1f1
%global xsessiondir %{_datadir}/xsessions
Name:           ratpoison
Version:        1.4.9
Release:        1%{?dist}
Summary:        Minimalistic window manager
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/ratpoison/
Source0:        http://download.savannah.gnu.org/releases/ratpoison/ratpoison-%{version}.tar.xz
Source1:	%{name}.desktop
Requires:       emacs-filesystem >= %{_emacs_version}
# oreon:deps
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  readline-devel
BuildRequires:  texinfo
# /oreon:deps
%description
Ratpoison is a simple window manager that relies solely on keyboard input as
opposed to keyboard and mouse input.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS -DHAVE_GETLINE"
%configure --disable-dependency-tracking
make %{?_smp_mflags}
%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{xsessiondir}
install -m 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{xsessiondir}/
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/allwindows.sh
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/clickframe.pl
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/genrpbindings
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/rpshowall.sh
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/rpws
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/split.sh
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
