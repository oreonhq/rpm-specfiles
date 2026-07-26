%global source0_hash 42f294bfc8e186d29da89d1f766071505a20a22776168a31bb3408e03fa7a9d7

%global gem_name unicode

Name:           rubygem-%{gem_name}
Version:        0.4.4.5
Release:        6%{?dist}
Summary:        Unicode normalization library for Ruby
License:        Ruby
URL:            https://github.com/blackwinter/unicode
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/blackwinter/unicode/issues/7
Source1:        https://www.ruby-lang.org/en/about/license.txt
# This is a C extension linked against MRI, it's not compatible with other 
# interpreters. So we require MRI specifically instead of ruby(release).
BuildRequires:  gcc
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel

%description
Unicode normalization library for Ruby.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

cp -p %{SOURCE1} .
%gemspec_add_file "license.txt"

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name} %{buildroot}%{gem_extdir_mri}/

find %{buildroot}%{gem_instdir}/tools -type f -name '*.rb' -print0 | xargs -0 chmod +x
find %{buildroot}%{gem_instdir}/tools -type f -name '*.rb' -print0 \
  | xargs -0 -n1 sed -i 's|/usr/local/bin/ruby|/usr/bin/ruby|'

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
ruby -Ilib:$(dirs +1)%{gem_extdir_mri} test/test.rb
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/license.txt
%{gem_extdir_mri}
%{gem_spec}
%{gem_libdir}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/tools
%{gem_instdir}/unicode.gemspec

%changelog
%autochangelog
