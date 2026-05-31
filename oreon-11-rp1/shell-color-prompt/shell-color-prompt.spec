%global source0_hash none

# testsuite currently git clones bats libraries
%bcond tests 0

Name:           shell-color-prompt
Version:        0.7.1
Release:        3%{?dist}
Summary:        Color prompt for bash shell

License:        GPL-2.0-or-later
URL:            https://github.com/juhp/bash-color-prompt
Source0:        bash-color-prompt.sh.in
Source1:        README.md
Source2:        COPYING
Source3:        Makefile
Source4:        gen.m4
Source10:       test.bats
BuildArch:      noarch
BuildRequires:  m4
BuildRequires:  make
%if %{with tests}
BuildRequires:  bats
BuildRequires:  git-core
BuildRequires:  hostname
%endif

%description
Default colored bash prompt.

%package -n bash-color-prompt
Summary:        Color prompt for bash shell

%description -n bash-color-prompt
Default colored bash prompt.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -c -T
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .


%build
make
sed -i -e "s/@BASHCOLORVERSION@/%{version}/" bash-color-prompt.sh


%install
%global profiledir %{_sysconfdir}/profile.d

install -m 644 -D -t %{buildroot}%{profiledir} bash-color-prompt.sh


%check
%if %{with tests}
mkdir -p tests
cd tests
cp  %{SOURCE10} .
BASH_COLOR_PROMPT_DIR=%{buildroot}%{profiledir} bats --timing --gather-test-outputs-in logs .
%endif


%files -n bash-color-prompt
%license COPYING
%doc README.md
%{profiledir}/bash-color-prompt.sh


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.1-3
- Prepare for Oreon 11 (RP1)
