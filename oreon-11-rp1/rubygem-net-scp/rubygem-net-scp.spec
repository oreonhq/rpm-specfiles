%global source0_hash b32ded0d48c88ce70844a063e4e14efb44a95e51a9e0c0bfb0c54b4313b622ea
%global gem_name net-scp
Summary:        A pure Ruby implementation of the SCP client protocol
Name: rubygem-%{gem_name}
Version: 4.0.0
Release:        1%{?dist}
License: MIT
URL: https://github.com/net-ssh/net-scp
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-test.tar.gz
Patch0: rubygem-net-scp-4.0.0-Fix-Mocha-deprecation-warning.patch
Patch1: rubygem-mocha-2.6.1-Fix-rake-test-fails-with-mocha-2-1-0-72.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(base64)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(net-ssh)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A pure Ruby implementation of the SCP client protocol

%package doc
Summary: Documentation for %{name}
Requires:%{name} = %{version}-%{release}
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

pushd %{_builddir}
%patch 0 -p1
%patch 1 -p1
popd

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/test .
ruby -Ilib:test test/test_all.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-net-scp-doc -f %{oreon_filedir}/rubygem-net-scp-doc.list

%changelog

%autochangelog
