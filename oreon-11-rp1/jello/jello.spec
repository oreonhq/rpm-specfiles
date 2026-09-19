%global source0_hash ef6c8906270a82f062bfbd5dd5af1b14c7d6e4c77aa436cae483e28be6942383

Name:           jello
Version:        1.6.1
Release:        %autorelease
Summary:        Query JSON at the command line with Python syntax

# SPDX
License:        MIT
URL:            https://github.com/kellyjonbrazil/jello
# GitHub archive contains tests; PyPI sdist does not.
Source:         %{url}/archive/v%{version}/jello-%{version}.tar.gz

BuildArch:      noarch

BuildSystem:            pyproject
BuildOption(install):   -l jello

%description
Query, filter, and transform JSON and JSON Lines at the command line with
Python syntax.

%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 man/*

%check -a
%{py3_test_envvars} ./runtests.sh

%files -f %{pyproject_files}
%doc ADVANCED_USAGE.md
%doc CHANGELOG
%doc README.md

%{_bindir}/jello
%{_mandir}/man1/jello.1*

%changelog
%autochangelog
