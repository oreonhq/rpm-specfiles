%global source0_hash 4c60a2b0a3b36685c83b80d5789401c2f678c1652e3288315a1551d811d9f83e
%global gem_name sassc
%define debug_package %{nil}
Name:           rubygem-%{gem_name}
Summary:        Use libsass with Ruby!
Version:        2.4.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/sass/sassc-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch:          %{url}/pull/242.patch
Patch:          00-disable-broken-tests.patch
Requires:       libsass
# oreon:deps
BuildRequires:  libsass
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(ffi)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-around)
BuildRequires:  rubygem(test_construct)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Use libsass with Ruby!

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gem_name}-%{version} -p1

# disable building bundled libsass
sed -i "/s\.extensions/d" ../%{gem_name}-%{version}.gemspec

%build

sed -i "s/libsass\.\#{dl_ext}/libsass\.\#{dl_ext}\.1/" lib/sassc/native.rb
sed -i "s!__dir__!\"%{_libdir}\"!" lib/sassc/native.rb
gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i '/require "pry"/ s/^/#/' test/test_helper.rb
ruby -Ilib -e 'Dir.glob "./test/**_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-sassc-doc -f %{oreon_filedir}/rubygem-sassc-doc.list

%changelog

%autochangelog
