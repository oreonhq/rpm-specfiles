%global source1_hash f5eb1b2956d5f7a67b2e5722a3749bc2fe86f9c580f2e3f5a08519cf073b5864
%global source0_hash 42f294bfc8e186d29da89d1f766071505a20a22776168a31bb3408e03fa7a9d7
%global gem_name unicode
Name:           rubygem-%{gem_name}
Version:        0.4.4.5
Release:        6%{?dist}
Summary:        Unicode normalization library for Ruby
License:        Ruby
URL:            https://github.com/blackwinter/unicode
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        https://www.ruby-lang.org/en/about/license.txt
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel
# /oreon:deps
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
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -Ilib:$(dirs +1)%{gem_extdir_mri} test/test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-unicode-doc -f %{oreon_filedir}/rubygem-unicode-doc.list

%changelog

%autochangelog
