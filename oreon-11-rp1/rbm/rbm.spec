%global source0_hash 2fd2aaa207efbe526f66fb03daf93ef4eb35acde315b060a9a737ac0cdfd5629
%global commit0 c6a40950607fa73861f81185764dff2bab150010
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Name:       rbm
Version:    0.4^20241205git%{shortcommit0}
Release:        1%{?dist}
Summary:        Reproducible Build Manager
License:    CC0-1.0
URL:        https://rbm.torproject.org/
Source0:        %{name}-%{shortcommit0}.tar.gz
Patch0:     rbm-c485326-Install-container-script-as-rmbcontainer.patch
Patch1:     rbm-c6a4095-Remove-on-line-tests.patch
BuildArch:  noarch
Requires:       bash
Requires:       bzip2
Requires:       coreutils
Requires:       dnf5
Requires:       git-core
Requires:       gnupg
Requires:       gzip
Requires:       hostname
Requires:       man-db
Requires:       mercurial
Requires:       perl(Exporter)
Requires:       redhat-lsb
Requires:       rpm
Requires:       rpm-build
Requires:       shadow-utils
Requires:       sudo
Requires:       tar
Requires:       util-linux-core
Requires:       wget
Requires:       xz
Requires:       zstd
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream
cp -a test test.pl %{buildroot}%{_libexecdir}/%{name}/upstream
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/upstream/* "$DIR"
pushd "$DIR"
./test.pl
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./test.pl
%files -f %{oreon_filedir}/main.list
%files -n rbm-tests -f %{oreon_filedir}/rbm-tests.list

%changelog

%autochangelog
