%global source0_hash f2c2d00230a0bf019a41ff128351f82bf6b9dc738f42181fe9b6c7167cb5d6b2

# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 1
# Run tests in check section
%global with_check 0
# Generate unit-test rpm
%global with_unit_test 0

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%global provider        github
%global provider_tld    com
%global project         kushaldas
%global repo            gotun
# https://github.com/kushaldas/gotun
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          a9dbe4dfa7ad8303528aff03072784d2c88331fd
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global aws_commit      1a651d9028d1203f4a0ba9fee91b207536cd4ca2

Name:           gotun
Version:        0
Release:        0.24.git%{shortcommit}%{?dist}
Summary:        Tool to run tests on OpenStack
# Detected licences
# - Unknown at 'COPYING'
# - Unknown at 'LICENSE'
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
ExclusiveArch: x86_64

%if ! 0%{?with_bundled}
# aws.go
# BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
# BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
# BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
# BuildRequires: golang(github.com/aws/aws-sdk-go/service/ec2)
# BuildRequires: golang(github.com/spf13/viper)
BuildRequires: golang(github.com/go-ini/ini)

# main.go
BuildRequires: golang(github.com/spf13/viper)
BuildRequires: golang(github.com/urfave/cli)

# openstack.go
BuildRequires: golang(github.com/rackspace/gophercloud)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/compute/v2/extensions/floatingip)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/compute/v2/extensions/keypairs)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/compute/v2/servers)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/imageservice/v2/images)
BuildRequires: golang(github.com/spf13/viper)
BuildRequires: golang(golang.org/x/crypto/ssh)

# utils.go
BuildRequires: golang(github.com/spf13/viper)
BuildRequires: golang(golang.org/x/crypto/ssh)

# Remaining dependencies not included in main packages
%endif

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

BuildRequires: golang(github.com/go-ini/ini)
Requires: golang(github.com/go-ini/ini)
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws)) = %{aws_commit}
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials)) = %{aws_commit}
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/session)) = %{aws_commit}
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/ec2)) = %{aws_commit}

%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{repo}-%{commit}

%build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../ src/%{import_path}

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{gopath}
%else
# take aws/aws-sdk-go from bundled deps
mv vendor/github.com/aws src/github.com/.
rm -rf vendor
export GOPATH=$(pwd):%{gopath}
%endif

%gobuild -o bin/gotun %{import_path}/

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 bin/gotun %{buildroot}%{_bindir}

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# Since we aren't packaging up the vendor directory we need to link 
# back to it somehow. Hack it up so that we can add the vendor
# directory from BUILD dir as a gopath to be searched when executing
# tests from the BUILDROOT dir.
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor

export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING LICENSE
%doc README.md
%{_bindir}/gotun

%if 0%{?with_devel}
%files devel -f devel.file-list
%license COPYING LICENSE
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license COPYING LICENSE
%doc README.md
%endif

%changelog
%autochangelog
