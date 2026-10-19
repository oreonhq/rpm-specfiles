%global source0_hash 34a3c8d41584069718eae52c56d449ba28d49b52263b032ec46934f789d80121
Name:           python-packbits
Version:        0.6
Release:        1%{?dist}
Summary:        PackBits encoder/decoder
License:        MIT
URL:            https://github.com/kmike/packbits
Source0:        https://github.com/kmike/packbits/archive/%{version}/packbits-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-packbits = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-packbits
Summary:        PackBits encoder/decoder
%description -n python3-packbits

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir packbits-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-packbits usr/lib/python3*/site-packages/packbits* usr/lib64/python3*/site-packages/packbits* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/packbits* usr/lib64/python3*/site-packages/packbits* usr/bin/*

%check

%tox
%files
%files -n python3-packbits -f %{oreon_filedir}/python3-packbits.list

%changelog

%autochangelog
