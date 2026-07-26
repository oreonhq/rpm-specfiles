%global source0_hash aea8a486b8b919ccd5b5ce6e3f2a8ea255858511915b3f9f8b30105e83436b0d

%if 0%{?rhel} > 7 || 0%{?fedora}
%global use_python3 1
%global use_python2 0
%global ourpythonbin %{__python3}
%global our_sitelib %{python3_sitelib}
%else
%global use_python3 0
%global use_python2 1
%if 0%{?__python2:1}
%global ourpythonbin %{__python2}
%global our_sitelib %{python2_sitelib}
%else
%global ourpythonbin %{__python}
%global our_sitelib %(%{ourpythonbin} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%endif
%endif

%if 0%{?rhel} == 7
%bcond check 1
%else
%bcond check 0
%endif

Name: tito
Version: 0.6.27
Release: 7%{?dist}
Summary: A tool for managing rpm based git projects

License: GPL-2.0-only
URL: https://github.com/rpm-software-management/tito
# Sources can be obtained by
# git clone https://github.com/rpm-software-management/tito
# cd tito
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
%if %{use_python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: python3-setuptools
Requires: python3-bugzilla
Requires: python3-blessed
Requires: rpm-python3
Recommends: python3-fedora-distro-aliases
%else
BuildRequires: python2-devel
BuildRequires: python-setuptools
Requires: python-setuptools
Requires: python-bugzilla
Requires: python-blessed
Requires: rpm-python
%endif
BuildRequires: asciidoc
BuildRequires: docbook-style-xsl
BuildRequires: libxslt
BuildRequires: rpmdevtools
BuildRequires: rpm-build
BuildRequires: tar
BuildRequires: which

%if %{with check}
BuildRequires: createrepo_c
BuildRequires: git
BuildRequires: rsync
BuildRequires: python3-blessed
BuildRequires: python3-bugzilla
BuildRequires: python3-pycodestyle
BuildRequires: python3-pytest
BuildRequires: python3-rpm
%endif

Requires: rpm-build
Requires: rpmlint
Requires: fedpkg
Requires: fedora-packager
Requires: rpmdevtools
# Cheetah used not to exist for Python 3, but it's what Mead uses.  We
# install it and call via the command line instead of importing the
# previously potentially incompatible code, as we have not yet got
# around to changing this
Requires: /usr/bin/cheetah

%description
Tito is a tool for managing tarballs, rpms, and builds for projects using
git.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n tito-%{version}

%build
%{ourpythonbin} setup.py build
# convert manages
a2x --no-xmllint -d manpage -f manpage titorc.5.asciidoc
a2x --no-xmllint -d manpage -f manpage tito.8.asciidoc
a2x --no-xmllint -d manpage -f manpage tito.props.5.asciidoc
a2x --no-xmllint -d manpage -f manpage releasers.conf.5.asciidoc

%install
rm -rf $RPM_BUILD_ROOT
%{ourpythonbin} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{our_sitelib}/*egg-info/requires.txt
# manpages
%{__mkdir_p} %{buildroot}%{_mandir}/man5
%{__mkdir_p} %{buildroot}%{_mandir}/man8
cp -a titorc.5 tito.props.5 releasers.conf.5 %{buildroot}/%{_mandir}/man5/
cp -a tito.8 %{buildroot}/%{_mandir}/man8/
# bash completion facilities
install -Dp -m 0644 share/tito_completion.sh %{buildroot}%{_datadir}/bash-completion/completions/tito

%if %{with check}
%check
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
./runtests.sh --no-cov
%endif

%files
%doc AUTHORS COPYING
%doc doc/*
%doc %{_mandir}/man5/titorc.5*
%doc %{_mandir}/man5/tito.props.5*
%doc %{_mandir}/man5/releasers.conf.5*
%doc %{_mandir}/man8/tito.8*
%{_bindir}/tito
%{_bindir}/generate-patches.pl
%{_datadir}/bash-completion/completions/tito
%dir %{our_sitelib}/tito
%{our_sitelib}/tito/*
%{our_sitelib}/tito-*.egg-info

%changelog
%autochangelog
