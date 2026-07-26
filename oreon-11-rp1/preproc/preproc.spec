%global source0_hash bb46b84e7886d278c7dd6c9ba62eb73dd6213490f17edb782e1c3acd87a6a869

# vim: syntax=spec

%if 0%{?fedora} || 0%{?rhel} > 7
%global python_pkg python3
%global python /usr/bin/python3
%else
%global python_pkg python2
%global python /usr/bin/python2
%endif

Name: preproc
Version: 0.5
Release: 15%{?dist}
Summary: Simple text preprocessor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://pagure.io/rpkg-util.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+ssh://git@pagure.io/rpkg-util.git#bcad4393160b3fe9f624ebdc0ac1a65dffd75754:preproc
%endif

# Source is created by:
# git clone https://pagure.io/rpkg-util.git
# cd rpkg-util/preproc
# git checkout preproc-0.5-1
# ./rpkg spec --sources
Source0: rpkg-util-preproc-bcad4393.tar.gz

# Upstream indicates non-maintenance (aside from security) and 3.11 in F37 deprecates the
# pipes module (it's been deprecated since 2.7?).
Patch0: 0001-pipes-to-shlex.patch

BuildArch: noarch

BuildRequires: %{python_pkg}
Requires: %{python_pkg}

%if 0%{?rhel} == 6
BuildRequires: python-argparse
Requires:      python-argparse
%endif

%description
Simple text preprocessor implementing a very basic templating language.
You can use bash code enclosed in triple braces in a text file and
then pipe content of that file to preproc. preproc will replace each of
the tags with stdout of the executed code and print the final renderred
result to its own stdout.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -T -b 0 -q -n rpkg-util-preproc
%patch -P0 -p1

%check
sed -i '1 s|#.*|#!%{python}|' preproc
./test

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 preproc %{buildroot}%{_bindir}

sed -i '1 s|#.*|#!%{python}|' %{buildroot}%{_bindir}/preproc

install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 man/preproc.1 %{buildroot}%{_mandir}/man1

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%{_bindir}/preproc
%{_mandir}/man1/preproc.1*

%changelog
%autochangelog
