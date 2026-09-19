%global source0_hash 2fd2aaa207efbe526f66fb03daf93ef4eb35acde315b060a9a737ac0cdfd5629

%global commit0 c6a40950607fa73861f81185764dff2bab150010
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       rbm
Version:    0.4^20241205git%{shortcommit0}
Release:    4%{?dist}
Summary:    Reproducible Build Manager
License:    CC0-1.0
# A bug tracker is at <https://gitlab.torproject.org/tpo/applications/rbm/>.
URL:        https://rbm.torproject.org/
# Latest 0.4 release is very old, use a git snapshot,
# <https://github.com/boklm/rbm/issues/2>.
# Upstream git repository is <https://git.torproject.org/builders/rbm.git>.
Source0:    %{name}-%{shortcommit0}.tar.gz
# Install container script, proposed to an upstream,
# <https://github.com/boklm/rbm/pull/8>.
Patch0:     rbm-c485326-Install-container-script-as-rmbcontainer.patch
# Remove tests which require the Internet, not suitable for an upstream.
Patch1:     rbm-c6a4095-Remove-on-line-tests.patch
BuildArch:  noarch
BuildRequires:  asciidoc
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Run-time:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(open)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Template)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML::XS)
# redhat-lsb and other tools are not used at tests
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# bash for /bin/sh defined in default configuration
Requires:       bash
Requires:       bzip2
# coreutils for chown, mktemp, rm, uname
Requires:       coreutils
# debuild not yet packaged
# dnf in default configuration,
Requires:       dnf5
Requires:       git-core
# gnupg for gpg defined in default configuration
Requires:       gnupg
Requires:       gzip
# hostname for hostname in container tool
Requires:       hostname
Requires:       man-db
Requires:       mercurial
Requires:       perl(Exporter)
# redhat-lsb for lsb_release
Requires:       redhat-lsb
# rpm in default configuration
Requires:       rpm
# rpm-build for rpmbuild defined in default configuration
Requires:       rpm-build
# shadow-utils for newuidmap, newgidmap in container tool
Requires:       shadow-utils
# sudo in default configuration
Requires:       sudo
# tar in default configuration
Requires:       tar
# util-linux-core for mount in container tool
Requires:       util-linux-core
# wget in default configuration
Requires:       wget
Requires:       xz
Requires:       zstd

%description
Reproducible Build Manager (rbm) is a tool that helps you create and build
packages for multiple Linux distributions, and automate the parts that can be
automated. It includes options to run the build in a defined environment to
allow reproducing the build.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl(RBM)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}
chmod +x test/projects/c/build
rm test/.gitignore

%build
%{make_build} sysconfigdir=%{_sysconfdir} bindir=%{_bindir} mandir=%{_mandir} \
    perldir=%{perl_vendorlib}

%install
%{make_install} sysconfigdir=%{_sysconfdir} bindir=%{_bindir} mandir=%{_mandir} \
    perldir=%{perl_vendorlib}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream
cp -a test test.pl %{buildroot}%{_libexecdir}/%{name}/upstream
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into ./test directory
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/upstream/* "$DIR"
pushd "$DIR"
./test.pl
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
./test.pl

%files
%license COPYING
%doc NEWS README.md TODO
%{_bindir}/rbm
%{_bindir}/rbmcontainer
%{perl_vendorlib}/RBM
%{perl_vendorlib}/RBM.pm
%{_mandir}/man1/rbm.*
%{_mandir}/man1/rbm-{build,fetch,showconf,tar,usage}.*
%{_mandir}/man7/rbm_{cli,config,input_files,layout,modules,remote,steps,targets,templates,tutorial}.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
