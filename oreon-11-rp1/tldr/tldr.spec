%global source0_hash 374e01c62148bb7142fdf79a8756dbd08408b3db2117b9f8c51e1ccab5f75d06
Name:           tldr
Version:        3.4.4
Release:        1%{?dist}
Summary:        Simplified and community-driven man pages
License:        MIT
URL:            https://github.com/tldr-pages/tldr-python-client
Source0:        https://github.com/tldr-pages/tldr-python-client/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tldr = %{version}-%{release}
# /oreon:deps
%package -n       python3-tldr+cli
Summary:        Metapackage for python3-tldr cli extras
Requires:       python3-tldr = %{version}-%{release}
Provides:       python3dist(tldr[cli]) = %{version}-%{release}

%description -n python3-tldr+cli
Metapackage for python3-tldr cli extras.

%description
A Python command line client for tldr - Simplified and community-driven
man pages http://tldr-pages.github.io/.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-python-client-%{version}
%oreon_prep
%build

pushd docs
make man
popd
%pyproject_wheel
%{python3} tldr.py --print-completion bash > tldr.bash
%{python3} tldr.py --print-completion zsh > tldr.zsh
%install
%pyproject_install
install -Dp --mode=0644 %{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dp --mode=0644 %{name}.zsh  %{buildroot}%{zsh_completions_dir}/_%{name}
rm -rf %{buildroot}%{_mandir}/man1/.doctrees/
%oreon_autofiles main

%check

%pytest -k "not test_error_message"
%files

%changelog

%autochangelog
