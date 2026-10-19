%global source1_hash 27ec821c678698948935c0f5a543ed16576e9d9538aa9622f8661841f19b4d7c
%global source0_hash 6d939919cfd81bcc4d6556f322c3995a70cfe4289ea0bd3b1f999b489c323088
%global gem_name execjs
Summary:        Run JavaScript code from Ruby
Name: rubygem-%{gem_name}
Version: 2.8.1
Release:        1%{?dist}
License: MIT
URL: https://github.com/rails/execjs
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/execjs/archive/refs/tags/v2.8.1.tar.gz
Patch0: rubygem-execjs-2.7.0-delete-JScript-and-json2.js.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  //bin/node
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
ExecJS lets you run JavaScript code from Ruby. It automatically picks the
best runtime available to evaluate your JavaScript program, then returns
the result to you as a Ruby object.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%patch 0 -p1
sed -i -e '/files/ s|"lib/execjs/support/jscript_runner.js".freeze, ||' \
    -e '/files/ s|"lib/execjs/support/json2.js".freeze, ||' %{gem_name}.gemspec

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
tar xzf %{SOURCE1}
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-execjs-doc -f %{oreon_filedir}/rubygem-execjs-doc.list

%changelog

%autochangelog
