%global source1_hash 39ca6bbe1d4f965d9648da001d2aed8b09f485e995c197010a02268f69da761c
%global source0_hash 04d62a06dd12bdd2dff1a2cde8a51339a1d37bb8471bc4cd97ef1f0b3be645d0
%global gem_name rake-contrib
Name: rubygem-%{gem_name}
Version: 1.0.0
Release:        1%{?dist}
Summary:        Additional libraries for Rake
License: MIT
URL: https://github.com/ruby/rake-contrib
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/ruby/rake-contrib/archive/refs/tags/v1.0.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(net-ftp)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Additional libraries for Rake.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
tar -xzf %{SOURCE1}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rake-contrib-doc -f %{oreon_filedir}/rubygem-rake-contrib-doc.list

%changelog

%autochangelog
