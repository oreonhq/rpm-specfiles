%global source1_hash 354dd0321710440a0b0e740b14135712cdd27e9faf92301360d659b12de80e62
%global source0_hash 3076e55132d43b21de93cd7c8149a8c1b2e4afc07e79855fb6b795a0ef20b051
%global gem_name asciidoctor-pdf
Name:     rubygem-%{gem_name}
Version:  2.3.24
Release:        1%{?dist}
Summary:        Converts AsciiDoc documents to PDF using Prawn
License:  MIT
URL:      https://github.com/asciidoctor/asciidoctor-pdf
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/asciidoctor/asciidoctor-pdf/archive/refs/tags/v2.3.24.tar.gz
Patch0: prawn-svg-0_36.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  poppler-utils
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(asciidoctor)
BuildRequires:  rubygem(chunky_png)
BuildRequires:  rubygem(coderay)
BuildRequires:  rubygem(concurrent-ruby)
BuildRequires:  rubygem(pdf-inspector)
BuildRequires:  rubygem(prawn)
BuildRequires:  rubygem(prawn-icon)
BuildRequires:  rubygem(prawn-svg)
BuildRequires:  rubygem(prawn-table)
BuildRequires:  rubygem(prawn-templates)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(rouge)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(safe_yaml)
BuildRequires:  rubygem(treetop)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
An extension for Asciidoctor that converts AsciiDoc documents to PDF using the
Prawn PDF library.

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
mv %{_builddir}/{spec,examples} .
mv %{_builddir}/docs/modules docs/
%patch -P0 -p1

# Regenerate the parser.
tt lib/asciidoctor/pdf/formatted_text/parser.treetop

%gemspec_remove_dep -g prawn-icon "~> 3.0.0"
%gemspec_add_dep -g prawn-icon "~> 3.0", ">= 3.0.0"
%gemspec_remove_dep -g prawn-svg "~> 0.34.0"
%gemspec_add_dep -g prawn-svg "~> 0.34", ">= 0.34.0"

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
rm -rf %{buildroot}%{gem_instdir}/.yardopts
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rspec -t '~network'
%files -f %{oreon_filedir}/main.list
%files -n rubygem-asciidoctor-pdf-doc -f %{oreon_filedir}/rubygem-asciidoctor-pdf-doc.list

%changelog

%autochangelog
