%global source0_hash aa92242fbe59077796309096cf2734c2d0e6c1c01f3a9a0a238620f8b20c541b

# Fedora review: https://bugzilla.redhat.com/show_bug.cgi?id=1503915

%if 0%{?rhel} == 7
%global __python %{__python2}
%global python python
%else
%global __python %{__python3}
%global python python3
%endif

%if 0%{?fedora} >= 30 || 0%{?rhel} > 7
%global bundle_pgpdump 1
%else
%global bundle_pgpdump 0
%endif

# Use symlinks instead of the EASY entry scripts
%bcond_with symlinks

Summary:	Key fingerprinting tools for CVE-2017-15361
Name:		roca-detect
Version:	1.2.12
Release:	34%{?dist}
License:	MIT
Url:		https://crocs.fi.muni.cz/public/papers/rsa_ccs17
Source0:	https://github.com/crocs-muni/roca/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	https://files.pythonhosted.org/packages/4d/ad/11339cf197a6b128a9b06725681a349f61a5dc778e1fe3b69e816a2d175b/pgpdump3-1.5.2.tar.gz

# Remove coloredlogs dependency as it is not in Fedora as of f28
# Also remove python3-future dependency for f41
Patch0:		roca-detect-color.patch
Patch1:		roca-detect-pkcs7.patch

BuildRequires:	%{python}-cryptography >= 3.2.1
%if !0%{bundle_pgpdump}
BuildRequires:	%{python}-pgpdump
%endif
BuildRequires:	%{python}-setuptools %{python}-devel
# Manual dependencies - in case auto dependency doesn't work
%if 0%{?rhel} == 7
Requires:	%{python}-cryptography %{python}-pgpdump
Requires:	%{python}-six
# el7 conflicts with python2-dateutil and doesn't work with python3
Requires:	python-dateutil
#Requires:	%%{python}-dateutil
%endif

BuildArch:	noarch

%{?python_enable_dependency_generator}

%description
This tool is related to the ACM CCS 2017 conference paper #124 Return of the
Coppersmith’s Attack: Practical Factorization of Widely Used RSA
Moduli.

https://crocs.fi.muni.cz/public/papers/rsa_ccs17

Install this to test public RSA keys for the presence of the vulnerability
described by CVE-2017-15361.

%if 0%{bundle_pgpdump}
%package -n python3-pgpdump
Summary: PGP packet parser library in Python 3.x
BuildArch: noarch

%description -n python3-pgpdump
python-pgpdump is a Python 3 library for parsing PGP packets. The intent here
is not on completeness, as we don't currently decode every packet type, but
on being able to do what people actually have to 95% of the time.

Currently supported things include:

* Signature packets
* Public key packets
* Secret key packets
* Trust, user ID, and user attribute packets
* ASCII-armor decoding and CRC check
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n roca-%{version}
%patch 0 -p0 -b .color
%patch 1 -p0 -b .pkcs7
%if 0%{bundle_pgpdump}
tar xvfz %{SOURCE1}
%endif

# remove leftover version control from upstream
find . -name .gitignore -delete

# fix env shbang in CLI scripts
%py_shebang_fix roca

# fix pgpdump requires
sed -i -e"s/'pgpdump'/'pgpdump3'/" setup.py

%build
%py_build
%if 0%{bundle_pgpdump}
cd pgpdump3-1.5.2
%py_build
%endif

%install
%py_install
%if 0%{bundle_pgpdump}
cd pgpdump3-1.5.2
%py_install
%endif

# make all CLI scripts executable to keep rpmlint happy, even though
# we are using EASY introducers instead.
chmod a+x `find %{buildroot}%{python_sitelib}/roca -name "*.py" | \
	xargs grep -l '^#!.*python'`

# Replace complex "EASY" universal wrapper with symlinks to cli scripts.
%if %{with symlinks}
ln -sf %{python_sitelib}/roca/detect.py %{buildroot}%{_bindir}/roca-detect
ln -sf %{python_sitelib}/roca/detect_tls.py %{buildroot}%{_bindir}/roca-detect-tls
%endif

%check
export PYTHONPATH=pgpdump3-1.5.2
%{__python} -m unittest discover

%files
%doc README.md docs
%license LICENSE
%{_bindir}/roca-detect*
%{python_sitelib}/roca
%{python_sitelib}/roca_detect-%{version}*

%if 0%{bundle_pgpdump}
%files -n python3-pgpdump
%doc pgpdump3-1.5.2/README.md
%license pgpdump3-1.5.2/COPYRIGHT
%{python_sitelib}/pgpdump*
%endif

%changelog
%autochangelog
