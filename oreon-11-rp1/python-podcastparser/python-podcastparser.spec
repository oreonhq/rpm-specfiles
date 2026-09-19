%global source0_hash 14322a32b300a0dbd307f7b19da0a0b2e024b7e62a961e9ddc698c473c4f5d3e

%global modname podcastparser
%global sum     Simplified, fast RSS parsing library

Name:               python-%{modname}
Version:            0.6.11
Release:            2%{?dist}
Summary:            %{sum}

License:            ISC
URL:                https://github.com/gpodder/%{modname}
Source0:            %{url}/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz

BuildRequires:      python3-devel

BuildArch:          noarch

%description
The podcast parser project is a library from the gPodder project to provide
an easy and reliable way of parsing RSS- and Atom-based podcast feeds in
Python.

%package -n python3-%{modname}
Summary:            %{sum}

%description -n python3-%{modname}
%{sum}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

# Better safe than sorry
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '%{modname}*'

%{!?_licensedir: %global license %doc}

%check
%pyproject_check_import

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
