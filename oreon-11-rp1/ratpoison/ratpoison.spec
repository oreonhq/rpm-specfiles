%global source0_hash d98fa4be025ecca453c407ff311ab3949f29f20d6d8abedf8f0716b85fc8d1f1

%global xsessiondir %{_datadir}/xsessions

Name:           ratpoison
Version:        1.4.9
Release:        30%{?dist}
Summary:        Minimalistic window manager
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/ratpoison/
Source0:        http://download.savannah.gnu.org/releases/ratpoison/ratpoison-%{version}.tar.xz
Source1:	%{name}.desktop
BuildRequires: make
BuildRequires:  gcc, texinfo
BuildRequires: libXft-devel, libX11-devel, perl-generators, readline-devel, libXt-devel, libXinerama-devel, libXtst-devel, libXi-devel, libXrandr-devel
BuildRequires:  emacs
Requires:       emacs-filesystem >= %{_emacs_version}

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

%files
%{_bindir}/ratpoison
%{_bindir}/rpws
%doc %{_datadir}/doc/ratpoison/
%{_infodir}/ratpoison.info.*
%{_mandir}/man1/ratpoison.1.gz
%{_datadir}/ratpoison/
%{_datadir}/xsessions/ratpoison.desktop
%{_emacs_sitelispdir}/*.el

%changelog
%autochangelog
