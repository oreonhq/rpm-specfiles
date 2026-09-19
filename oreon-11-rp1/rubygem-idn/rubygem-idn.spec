%global source0_hash b090e317b98247fd701449e54fa5ed35e4f1cbfd934a8fe1bb12792ce9b80a32

# Generated from idn-0.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name idn

Name: rubygem-%{gem_name}
Version: 0.0.2
Release: 51%{?dist}
Summary: Ruby Bindings for the GNU LibIDN library
# ASL license for ext/idn.c, ext/idn.h, ext/punycode.c and ext/stringprep.c
# Automatically converted from old format: ASL 2.0 and LGPLv2+ - review is highly recommended.
License: Apache-2.0 AND LicenseRef-Callaway-LGPLv2+
URL: http://rubyforge.org/projects/idn/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-idn-0.0.2-Fix-for-ruby-1.9.x.patch
# Fixes failure due to change in default encoding in Ruby 2.0.
# http://rubyforge.org/tracker/index.php?func=detail&aid=29724&group_id=924&atid=3635
Patch1: rubygem-idn-0.0.2-ruby2-encoding-in-tests-fix.patch

Patch2: rubygem-idn-c99.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: libidn-devel
BuildRequires: rubygem(test-unit)

%description
Ruby Bindings for the GNU LibIDN library, an implementation of the Stringprep,
Punycode and IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group. 

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
ruby -I$(dirs +1)%{gem_extdir_mri} -e 'Dir.glob "./test/tc_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE
%exclude %{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/NOTICE
%doc %{gem_instdir}/README
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
%autochangelog
