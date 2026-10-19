%global source0_hash 8a25bdfc0f991701554e7982523780de78f2b4de5a55a2a378828c3299204d36
Name:		wult
Version:	1.12.48
Release:        1%{?dist}
Summary:        A tool for measuring C-state latency in Linux
License:	BSD-3-Clause AND GPL-2.0-only
Url:		https://github.com/intel/wult
Source0:        https://github.com/intel/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		exclude-dirs.patch
ExclusiveArch:	x86_64
Requires:	pciutils
Requires:	pepc
Requires:	python3-%{name} = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wult = %{version}-%{release}
# /oreon:deps
%description
The name Wult comes from "Wake Up Latency Tracer". Wult measures C-state
latency by scheduling a delayed interrupt at a known time in the future, so it
relies on devices allowing for delayed interrupts. Today wult can use LAPIC as
the source of delayed interrupts, as well as I210 PCIe Gigabit Ethernet
adapter. However, other devices could be supported as well, for example other
Intel Ethernet adapters.

%package -n python3-%{name}
Summary:	Wult Python library
BuildArch:	noarch
%description -n python3-%{name}
Wult Python libraries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%make_build -C helpers/ndl-helper
%make_build -C helpers/wult-freq-helper
%install
%pyproject_install
install -pDm755 helpers/ndl-helper/ndl-helper %{buildroot}%{_bindir}/ndl-helper
install -pDm755 helpers/wult-freq-helper/wult-freq-helper %{buildroot}%{_bindir}/wult-freq-helper
%oreon_autofiles main usr/lib/python3*/site-packages/wult* usr/lib64/python3*/site-packages/wult* usr/bin/*

%check

%pytest -v
%files
%files -n python3-wult -f %{oreon_filedir}/python3-wult.list

%changelog

%autochangelog
