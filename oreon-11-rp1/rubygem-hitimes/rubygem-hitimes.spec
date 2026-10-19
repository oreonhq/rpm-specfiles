%global source1_hash f0307ef69dabf3b8f419e9e0f1d4596807c9dece0bca8ec931355e168d1fc395
%global source0_hash ad2ee849910cd3a6c37c4aec3f1b82df69eaf0233e36c60f02009bf3d20447f5
%global gem_name hitimes
Name: rubygem-%{gem_name}
Version: 3.0.0
Release:        4%{?dist}
Summary:        A fast, high resolution timer library for recording performance metrics
License: ISC
URL: http://github.com/copiousfreetime/hitimes
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/copiousfreetime/hitimes/archive/refs/tags/v3.0.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Hitimes is a fast, high resolution timer library for recording performance
metrics. It uses the internal ruby `Process::clock_gettime()` to get the highest
granularity time increment possible. Generally this is nanosecond resolution, or
whatever the hardware in the CPU supports.

%package doc
Summary: Documentation for %{name}
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
ln -s %{_builddir}/spec spec
sed -i '/minitest\/focus/ s/focus/autorun/' spec/spec_helper.rb
ruby -Ilib:spec -e 'Dir.glob "./spec/*spec.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-hitimes-doc -f %{oreon_filedir}/rubygem-hitimes-doc.list

%changelog

%autochangelog
