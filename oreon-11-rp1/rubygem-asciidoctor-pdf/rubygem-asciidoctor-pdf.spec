%global source0_hash 3076e55132d43b21de93cd7c8149a8c1b2e4afc07e79855fb6b795a0ef20b051

%global gem_name asciidoctor-pdf

Name:     rubygem-%{gem_name}
Version:  2.3.24
Release:  2%{?dist}
Summary:  Converts AsciiDoc documents to PDF using Prawn
License:  MIT
URL:      https://github.com/asciidoctor/asciidoctor-pdf
Source0:  https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/asciidoctor/asciidoctor-pdf.git && cd asciidoctor-pdf
# git checkout v2.3.24
# tar -czf rubygem-asciidoctor-pdf-2.3.24-specs-examples.tgz spec/ examples/ docs/
Source1:  %{name}-%{version}-specs-examples.tgz
Patch0: prawn-svg-0_36.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 3.5.9
BuildRequires: ruby >= 3.3
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(asciidoctor)
BuildRequires: rubygem(prawn)
BuildRequires: rubygem(prawn-svg)
BuildRequires: rubygem(prawn-table)
BuildRequires: rubygem(prawn-templates)
BuildRequires: rubygem(prawn-icon)
BuildRequires: rubygem(treetop)
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(safe_yaml)
BuildRequires: rubygem(chunky_png)
BuildRequires: rubygem(pdf-inspector)
BuildRequires: rubygem(rouge)
BuildRequires: rubygem(coderay)
BuildRequires: rubygem(rexml)
BuildRequires: poppler-utils

BuildArch: noarch

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

%check
rspec -t '~network'

%files
%dir %{gem_instdir}
%{_bindir}/%{gem_name}
%{_bindir}/%{gem_name}-optimize
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.adoc
%{gem_instdir}/bin
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/NOTICE.adoc
%doc %{gem_instdir}/CHANGELOG.adoc
%doc %{gem_instdir}/docs
%{gem_instdir}/%{gem_name}.gemspec

%changelog
%autochangelog
