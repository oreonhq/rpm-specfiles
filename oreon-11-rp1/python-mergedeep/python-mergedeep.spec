%global source0_hash 7d44051cce4de6a870bc08642e561e9d2b0c09b261e9fb709a5489f44699f551

Name:           python-mergedeep
Version:        1.3.4
Release:        20%{?dist}
Summary:        A deep merge function for python
BuildArch:      noarch

License:        MIT
URL:            https://github.com/clarketm/mergedeep
Source0:        https://github.com/clarketm/mergedeep/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
A deep merge function for python.

%package -n python3-mergedeep
Summary:        %{summary}

%description -n python3-mergedeep
A deep merge function for python.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mergedeep-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mergedeep

%check
%tox

%files -n python3-mergedeep -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
