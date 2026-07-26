%global source0_hash 4ee1b40fef95fba589306842fd1f72bd7902f4dcd89af8fd80931913e5e71d0d

%global         usegit      1
%global         baserelease     29

%global         githash     ff9cd266b9700b19c15a4b3cb7104134b5398133
%global         shorthash   %(TMP=%githash ; echo ${TMP:0:10})
%global         gitdate     Mon 14 Apr 2025 08:18:48 +0100
%global         gitdate_num 20250404

%if 0%{?usegit} >= 1
%global         fedorarel   0.%{baserelease}.D%{gitdate_num}git%{shorthash}
%else
%global         fedorarel   %{?prever:0.}%{baserelease}%{?prever:.%{prerpmver}}
%endif

%global	description_common \
This is a Python script to convert the output from prof, gprof, oprofile,\
Shark, AQtime, and python profilers into a dot graph.  It has the following\
features:\
\
* can correctly parse C++ template function names\
* allows to prune nodes and edges below a certain threshold\
* uses an heuristic to propagate time inside mutually recursive functions\
* uses color efficiently to draw attention to hot-spots\
%{nil}

Name:           gprof2dot
Version:        1.0
Release:       	%{fedorarel}%{?dist}
Summary:        Generate dot graphs from the output of several profilers

# SPDX confirmed
License:        LGPL-3.0-or-later
URL:            https://github.com/jrfonseca/gprof2dot
Source0:        https://github.com/jrfonseca/gprof2dot/archive/%{githash}/%{name}-%{version}-D%{gitdate_num}git%{githash}.tar.gz
BuildArch:      noarch

Obsoletes:      python2-%{name} < 1.0-0.17
Obsoletes:      python3-%{name} < 1.0-0.17
Obsoletes:      %{name}-python3 < 1.0-0.17
BuildRequires:  python3
BuildRequires:  graphviz

%global _description\
%description_common

%description %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{githash}

%build

%install
mkdir -p %{buildroot}%{_bindir}

install -p -m 0755 gprof2dot.py %{buildroot}%{_bindir}/gprof2dot
sed -i %{buildroot}%{_bindir}/gprof2dot \
	-e 's|/usr/bin/env[ \t][ \t]*python$|%{_bindir}/python3|'

%check
python3 ./tests/test.py

%files
%license LICENSE.txt
%doc README.md
%doc sample.svg
%doc schema.json

%{_bindir}/gprof2dot

%changelog
%autochangelog
