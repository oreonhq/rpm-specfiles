%global source0_hash cf3b3ce63ffd20a9ac4378a06f313a2157e4244ce78637671bf10a91797d1164

# Generated from ruby-libvirt-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-libvirt

Summary: Ruby bindings for LIBVIRT
Name: rubygem-%{gem_name}
Version: 0.8.4
Release: 7%{?dist}
License: LGPL-2.1-or-later
URL: http://libvirt.org/ruby/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: libvirt-daemon-kvm
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: libvirt-devel
BuildRequires: gcc

ExcludeArch: %{ix86}

%description
Ruby bindings for libvirt.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build
export CONFIGURE_ARGS="--with-cflags='%{build_cflags} -fPIC'"
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# remove shebangs from test files
pushd %{buildroot}%{gem_instdir}/tests
find -type f -name '*.rb' -print | xargs sed -i '/#!\/usr\/bin\/ruby/d'
popd

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext

%check
pushd .%{gem_instdir}

ruby -Ilib:%{buildroot}%{gem_extdir_mri}:test  -e "Dir.glob('./tests/**/test_*.rb').sort.each {|t| require t}"

popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/COPYING
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/NEWS.rst
%doc %{gem_instdir}/README.rst
%doc %{gem_instdir}/doc/main.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/tests

%changelog
%autochangelog
