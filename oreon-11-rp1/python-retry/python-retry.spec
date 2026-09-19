%global source0_hash 9bffdf1a1cee51602b7bc6cc00dfac13d89528aaef34f5bd8f596d2b1ef1b7d8

Name:           python-retry
Version:        0.9.4
Release:        14%{?dist}
Summary:        Easy to use retry decorator

License:        Apache-2.0
URL:            https://github.com/eSAMTrade/retry
Source:         %{url}/archive/%{version}/retry-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# https://github.com/eSAMTrade/retry/pull/7
# https://github.com/eSAMTrade/retry/pull/8
Patch:          fix_requirements.patch

%global _description %{expand:
Easy to use retry decorator}

%description %_description

%package -n python3-retry
Summary:        %{summary}

%description -n python3-retry %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n retry-%{version}

%generate_buildrequires
export PBR_VERSION="%{version}"
%pyproject_buildrequires -t

%build
export PBR_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files retry

%check
%tox

%files -n python3-retry -f %{pyproject_files}
%doc README.* ChangeLog AUTHORS
%license LICENSE

%changelog
%autochangelog
