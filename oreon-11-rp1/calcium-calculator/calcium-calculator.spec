%global source0_hash 6af463890d929aa22412c8cee3316e1c3bd1860aceee576b975526091bac64f1
%global forgeurl https://github.com/mvvik/CalC-complex-buffer
%bcond freeglut 1
Name:       calcium-calculator
Version:    7.10.6
Release:        1%{?dist}
Summary:        The Calcium Calculator
%global tag v%{version}
%forgemeta
License:    GPL-3.0-only
URL:        https://web.njit.edu/~matveev/calc.html
Source0:        %{forgeurl}/archive/%{tag}/CalC-complex-buffer-%{version}.tar.gz
Patch:      Makefile_v7.10.7.patch
Patch:      include_local_CXXFLAGS.patch
%if %{with freeglut}
%endif
# oreon:deps
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  make
# /oreon:deps
%description
CalC ("Calcium Calculator") is a free (GNU copyleft) modeling tool for
simulating intracellular calcium diffusion and buffering. CalC solves
continuous reaction-diffusion PDEs describing the entry of calcium into a
volume through point-like channels, and its diffusion, buffering and binding to
calcium receptors.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1 -S git

find . -name "*" -type f -exec chmod 0644 '{}' \;
find . -name "*" -type f -exec sed -i 's/\r$//' '{}' \;

%build

%{set_build_flags}
%if %{with freeglut}
%make_build
%else
%make_build noGraphs
%endif
%install
mv -v CalC %{name}
install -p -m 755 -D -t $RPM_BUILD_ROOT/%{_bindir} %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
