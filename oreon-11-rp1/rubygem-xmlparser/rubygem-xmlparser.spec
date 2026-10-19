%global source0_hash f9681a75ca15010a7e0f0d3ad016b291d2fe527b8110627021cb845e1ff02755
%global gem_name xmlparser
Summary:        Ruby bindings to the Expat XML parsing library
Name: rubygem-%{gem_name}
Version: 0.7.2.1
Release:        1%{?dist}
Group: Development/Languages
License: GPL-2.0-or-later and (  Ruby or GPL-2.0-or-later or MIT ) and (  GPL-1.0-or-later OR Artistic-1.0-Perl )
URL: http://rubygems.org/gems/xmlparser
Source0:        http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-xmlparser-ftbfs-fix.patch
Patch1: rubygem-xmlparser-enc_to_encindex-fix.patch
Patch2: rubygem-xmlparser-c99.patch
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  perl
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  ruby(rubygems)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(mkrf)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby bindings to the Expat XML parsing library. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

gem build %{gem_name}.gemspec
%gem_install
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -rp .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/ext
mkdir -p %{buildroot}%{gem_extdir_mri}/
cp -a ./%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
