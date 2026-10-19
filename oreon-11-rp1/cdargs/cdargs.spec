%global source0_hash ee35a8887c2379c9664b277eaed9b353887d89480d5749c9ad957adf9c57ed2c
%define    profiledir    %{_sysconfdir}/profile.d
Name:       cdargs
Version:    1.35
Release:        1%{?dist}
Summary:        The shell cd with bookmarks and browser
License:    GPL-2.0-or-later
URL:        http://www.skamphausen.de/cgi-bin/ska/CDargs/
Source0:        http://www.skamphausen.de/downloads/cdargs/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}_emacs-init.el
Patch0:     %{name}-%{version}_shebangs.patch
Patch1:     %{name}-%{version}_format_security.patch
Patch2:     %{name}-%{version}_fix_fsf_address.patch
Patch3:     %{name}-%{version}_configure_c99.patch
Requires:         emacs-filesystem >= %{_emacs_version}
# oreon:deps
BuildRequires:  emacs
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Enables the user to quickly change working directory by navigating cd arguments
and expanding the shell built-in cd with bookmarks and browser.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%{_emacs_bytecompile} contrib/cdargs.el
%install
%make_install
mkdir -p %{buildroot}%{profiledir}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}
install -p -m 644 contrib/cdargs.el* %{buildroot}%{_emacs_sitelispdir}/%{name}
install -p -m 644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/cdargs-init.el
install -p -m 644 contrib/cdargs-bash.sh %{buildroot}%{profiledir}/cdargs.sh
install -p -m 644 contrib/cdargs-tcsh.csh %{buildroot}%{profiledir}/cdargs.csh
install -D -p -m 644 src/cdargs.h %{buildroot}%{_includedir}/cdargs.h
%oreon_autofiles cdargs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cdargs-devel -f %{oreon_filedir}/cdargs-devel.list

%changelog

%autochangelog
