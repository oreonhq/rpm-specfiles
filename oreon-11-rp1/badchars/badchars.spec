%global source0_hash b5d865d311b21b1db720704e34704427079ba7a3fdeeea23647f39ba62d5444b
%global pypi_name badchars
Name:           %{pypi_name}
Version:        0.5.0
Release:        4%{?dist}
Summary:        HEX bad char generator for different programming languages
License:        MIT
URL:            https://github.com/cytopia/badchars
Source0:        https://github.com/cytopia/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-badchars = %{version}-%{release}
# /oreon:deps
%description
A HEX bad char generator to instruct encoders such as shikata-ga-nai to
transform those to other chars.

%package -n     python3-%{pypi_name}
Summary:        HEX bad char generator for different programming languages
%description -n python3-%{pypi_name}
A HEX bad char generator to instruct encoders such as shikata-ga-nai to
transform those to other chars.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-badchars usr/lib/python3*/site-packages/badchars* usr/lib64/python3*/site-packages/badchars* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/badchars* usr/lib64/python3*/site-packages/badchars* usr/bin/*

%files
%files -n python3-badchars -f %{oreon_filedir}/python3-badchars.list

%changelog

%autochangelog
