%global source0_hash cc56837be973d1a102dc6936a0b7235a1d716c0f7cd053bf77e0620577cff986

Name:           avra
Version:        1.4.2
Release:        12%{?dist}
Summary:        Atmel AVR assembler

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/Ro5bert/avra
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/Ro5bert/avra/pull/49
Patch0:         avra-1.4.2-fixes.patch
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

%description
Avra is an assembler for Atmel's AVR 8-bit RISC microcontollers.
It is mostly compatible with Atmel's own assembler, but provides new features
such as better macro support and additional preprocessor directives.
This package also contains various device definition files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
make %{?_smp_mflags} PREFIX=%{_prefix} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" TARGET_INCLUDE_PATH=%{_datadir}/%{name}

%install
%make_install PREFIX=%{_prefix} TARGET_INCLUDE_PATH=%{_datadir}/%{name}

mkdir -p %{buildroot}/%{_datadir}/%{name}/
install -p -m 0644 includes/*.inc %{buildroot}/%{_datadir}/%{name}/

%check
pushd tests/regression
./runtests.sh
popd

%files
%license COPYING
%doc AUTHORS TODO README.md USAGE.md examples/
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
%autochangelog
