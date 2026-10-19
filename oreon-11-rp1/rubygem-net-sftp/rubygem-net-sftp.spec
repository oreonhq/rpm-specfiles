%global source1_hash e4e695e4978f382ac8fd5ab953a09617dd3dd5507056b3a2fd866f31417891a2
%global source0_hash 65bb91c859c2f93b09826757af11b69af931a3a9155050f50d1b06d384526364
%global gem_name net-sftp
Name: rubygem-%{gem_name}
Version: 4.0.0
Release:        1%{?dist}
Summary:        A pure Ruby implementation of the SFTP client protocol
License: MIT
URL: https://github.com/net-ssh/net-sftp
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/net-ssh/net-sftp/archive/refs/tags/v4.0.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(base64)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(net-ssh)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A pure Ruby implementation of the SFTP client protocol.

%package doc
Summary: Documentation for %{name}
License: MIT AND LGPL-2.1-only
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/test .
ruby -Ilib:test test/test_all.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-net-sftp-doc -f %{oreon_filedir}/rubygem-net-sftp-doc.list

%changelog

%autochangelog
