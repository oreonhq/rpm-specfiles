%global source0_hash d77e979dc3a0b18e95fe2b61f45e5a765cb5661d52507019cf307929f50f65a9
%global gap_pkgname zeromqinterface
%global gap_upname  ZeroMQInterface
%global giturl      https://github.com/gap-packages/ZeroMQInterface
Name:           gap-pkg-%{gap_pkgname}
Version:        0.18
Release:        1%{?dist}
Summary:        ZeroMQ bindings for GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/ZeroMQInterface/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin gap tst
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  python3-devel
# /oreon:deps
%description
This package provides both low-level bindings as well as some higher level
interfaces for the ZeroMQ message passing library for GAP and HPC-GAP,
enabling lightweight distributed computation.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Documentation for ZeroMQ bindings for GAP
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
# Fix python shebang
sed -i.orig 's,%{_bindir}/env python,%{python3},' zgap
touch -r zgap.orig zgap
rm zgap.orig

%build -p

%configure --with-gaproot=%{gap_archdir}
%make_build
%install -a
mkdir -p %{buildroot}%{gap_archdir}/bin
cp -p zgap %{buildroot}%{gap_archdir}/bin
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-zeromqinterface-doc -f %{oreon_filedir}/gap-pkg-zeromqinterface-doc.list

%changelog

%autochangelog
