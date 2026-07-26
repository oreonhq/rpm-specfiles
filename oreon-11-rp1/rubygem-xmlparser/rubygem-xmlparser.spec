%global source0_hash f9681a75ca15010a7e0f0d3ad016b291d2fe527b8110627021cb845e1ff02755

%global gem_name xmlparser

Summary: Ruby bindings to the Expat XML parsing library
Name: rubygem-%{gem_name}
Version: 0.7.2.1
Release: 49%{?dist}
Group: Development/Languages
# src/lib/xml/xpath.rb is GPLv2+
# src/ext/encoding.h and the functions of encoding map are GPLv2+ or Artistic
# All other files are Ruby or GPLv2+ or MIT
# For a breakdown of the licensing, see also README
License: GPL-2.0-or-later and (  Ruby or GPL-2.0-or-later or MIT ) and (  GPL-1.0-or-later OR Artistic-1.0-Perl )
URL: http://rubygems.org/gems/xmlparser
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# Handle 'format not a string literal and no format arguments' error.
# https://bugzilla.redhat.com/show_bug.cgi?id=1037312
# Thanks to Gregor Herrmann for the patch.
# https://www.mail-archive.com/debian-bugs-rc@lists.debian.org/msg297233.html
Patch0: rubygem-xmlparser-ftbfs-fix.patch
Patch1: rubygem-xmlparser-enc_to_encindex-fix.patch
Patch2: rubygem-xmlparser-c99.patch
BuildRequires: perl
BuildRequires: ruby
BuildRequires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
BuildRequires: rubygem(rake)
BuildRequires: rubygem(mkrf)
BuildRequires: expat-devel

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

# remove development stuff
rm -rf %{buildroot}%{gem_instdir}/ext

# install externals
mkdir -p %{buildroot}%{gem_extdir_mri}/
cp -a ./%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

%files
%{gem_extdir_mri}
%dir %{gem_instdir}/
%doc %{gem_instdir}/[A-Z]*
%doc %{gem_docdir}
%{gem_instdir}/[a-z]*
%exclude %{gem_cache}
%{gem_spec}

%changelog
%autochangelog
