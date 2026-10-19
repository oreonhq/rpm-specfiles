%global source0_hash 59ab62fd8a4d0dfbde45009f87eb6f158ab2628a7c48886b0256f175166baaa8
%global gem_name msgpack
Name: rubygem-%{gem_name}
Version: 1.7.2
Release:        1%{?dist}
Summary:        MessagePack, a binary-based efficient data interchange format
License: Apache-2.0
URL: http://msgpack.org/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-spec.txz
Patch0:  msgpack-1.7.2-ruby34-format.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
MessagePack is a binary-based efficient object serialization library. It
enables to exchange structured objects between many languages like JSON. But
unlike JSON, it is very fast and small.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{builddir}/spec
%patch -P0 -p2
)

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -ar .%{gem_extdir_mri}/{gem.build_complete,%{gem_name}} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%ifnarch ppc64le
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{builddir}/spec spec
rm -rf spec/jruby
rspec -Ilib -I%{buildroot}%{gem_extdir_mri} spec
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-msgpack-doc -f %{oreon_filedir}/rubygem-msgpack-doc.list

%changelog

%autochangelog
