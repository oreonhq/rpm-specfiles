%global source1_hash 44fe4243a6a0cf4f7f953742f396559e4e4615b1794f35fa3b6e21f737fa2081
%global source0_hash 31cafc3ba73128e3c32791c9c8ddc2ee54d1cb3eac8161f73d9ecea809bee412
%global gem_name ref
Name: rubygem-%{gem_name}
Version: 2.0.0
Release:        1%{?dist}
Summary:        Library that implements weak, soft, and strong references in Ruby
License: MIT
URL: http://github.com/ruby-concurrency/ref
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/ruby-concurrency/ref/archive/refs/tags/v2.0.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Library that implements weak, soft, and strong references in Ruby that work
across multiple runtimes (MRI,Jruby and Rubinius). Also includes
implementation of maps/hashes that use references and a reference queue.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
tar xf %{SOURCE1}
sed -i '/[Cc]overalls/ s/^/#/' spec/spec_helper.rb
sed -i '/simplecov/ s/^/#/' spec/spec_helper.rb
sed -i '/SimpleCov/,/^end$/ s/^/#/' spec/spec_helper.rb
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ref-doc -f %{oreon_filedir}/rubygem-ref-doc.list

%changelog

%autochangelog
