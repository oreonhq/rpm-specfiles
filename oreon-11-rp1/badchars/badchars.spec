%global source0_hash b5d865d311b21b1db720704e34704427079ba7a3fdeeea23647f39ba62d5444b

%global pypi_name badchars

Name:           %{pypi_name}
Version:        0.5.0
Release:        4%{?dist}
Summary:        HEX bad char generator for different programming languages

License:        MIT
URL:            https://github.com/cytopia/badchars
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A HEX bad char generator to instruct encoders such as shikata-ga-nai to
transform those to other chars.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A HEX bad char generator to instruct encoders such as shikata-ga-nai to
transform those to other chars.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -M

%files
%{_bindir}/%{pypi_name}

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
