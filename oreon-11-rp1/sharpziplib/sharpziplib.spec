%global source0_hash 086c52dd98de17ffcc9f42310bf166a69718c829b413b9ea831fb296e2216a69

%global libname SharpZipLib

# mono is without any packagable debuginfo
%global debug_package %{nil}

%bcond_with brokentests

Name:           sharpziplib
Version:        1.3.3
Release:        10%{?dist}
Summary:        Zip, GZip, Tar and BZip2 library

# - as stated on the homepage, license is aka GNU Classpath exception:
# As a special exception, the copyright holders of this library give you permission
# to link this library with independent modules to produce an executable, regardless
# of the license terms of these independent modules, and to copy and distribute the
# resulting executable under terms of your choice, provided that you also meet, for
# each linked independent module, the terms and conditions of the license of that module. 
# - some files are licensed explicitly with BSD:
# + samples/cs/CreateZipFile/Main.cs
# + samples/cs/FastZip/Main.cs
# + samples/cs/minibzip2/Main.cs
# + samples/cs/minigzip/Main.cs
# + samples/cs/sz/sz.cs
# + samples/cs/tar/Main.cs
# + samples/cs/unzipfile/UnZipFile.cs
# + samples/cs/zipfiletest/ZipFileTest.cs
# + samples/vb/CreateZipFile/MainForm.vb
# + samples/vb/minibzip2/Main.vb
# + samples/vb/viewzipfile/Main.vb
# - samples/HttpCompressionModule is licensed as zlib/libpng (=zlib)
# Automatically converted from old format: GPLv2+ with exceptions and BSD and zlib - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2+-with-exceptions AND LicenseRef-Callaway-BSD AND Zlib
URL:            http://icsharpcode.github.io/%{libname}
Source0:        https://github.com/icsharpcode/%{name}/archive/v%{version}.tar.gz#/%{libname}-%{version}.tar.gz

ExclusiveArch:  %{mono_arches}
BuildRequires:  mono-devel

# fix ownership of mono folders
Requires:       mono-core

%description
SharpZipLib, formerly NZipLib is a Zip, GZip, Tar and BZip2 library
written entirely in C# . It is implemented as an assembly (installable
in the GAC), and thus can easily be incorporated into other projects.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn%{libname}-%{version}

%build

mkdir bin
cd src/ICSharpCode.SharpZipLib/

cat > AssemblyInfo.cs << FINISH
using System.Reflection;

// General Information about an assembly is controlled through the following 
// set of attributes. Change these attribute values to modify the information
// associated with an assembly.
[assembly: AssemblyTitle("SharpZipLib")]
[assembly: AssemblyVersion("%{version}")]
[assembly: AssemblyDescription("C# Zip, GZip, Tar and BZip2 library for .NET")]
[assembly: AssemblyCulture("")]
FINISH

mcs ./Lzw/LzwException.cs ./Lzw/LzwInputStream.cs ./Lzw/LzwConstants.cs ./Core/Exceptions/StreamDecodingException.cs \
    ./Core/Exceptions/SharpZipBaseException.cs ./Core/Exceptions/ValueOutOfRangeException.cs \
    ./Core/Exceptions/StreamUnsupportedException.cs ./Core/Exceptions/UnexpectedEndOfStreamException.cs \
    ./Core/EmptyRefs.cs \
    ./Core/InvalidNameException.cs ./Core/FileSystemScanner.cs ./Core/INameTransform.cs ./Core/PathFilter.cs \
    ./Core/PathUtils.cs ./Core/StreamUtils.cs ./Core/IScanFilter.cs ./Core/NameFilter.cs \
    ./BZip2/BZip2.cs ./BZip2/BZip2Exception.cs ./BZip2/BZip2InputStream.cs ./BZip2/BZip2OutputStream.cs ./BZip2/BZip2Constants.cs \
    ./Zip/ZipHelperStream.cs ./Zip/FastZip.cs ./Zip/IEntryFactory.cs ./Zip/Compression/InflaterHuffmanTree.cs \
    ./Zip/Compression/InflaterDynHeader.cs ./Zip/Compression/Deflater.cs ./Zip/Compression/DeflaterEngine.cs \
    ./Zip/Compression/DeflaterHuffman.cs ./Zip/Compression/DeflaterConstants.cs ./Zip/Compression/PendingBuffer.cs \
    ./Zip/Compression/Streams/InflaterInputStream.cs ./Zip/Compression/Streams/StreamManipulator.cs \
    ./Zip/Compression/Streams/DeflaterOutputStream.cs ./Zip/Compression/Streams/OutputWindow.cs ./Zip/Compression/Inflater.cs \
    ./Zip/Compression/DeflaterPending.cs ./Zip/ZipException.cs ./Zip/ZipEntryFactory.cs ./Zip/ZipFile.cs ./Zip/ZipExtraData.cs \
    ./Zip/ZipEntryExtensions.cs \
    ./Zip/ZipEntry.cs ./Zip/ZipNameTransform.cs ./Zip/ZipInputStream.cs ./Zip/ZipOutputStream.cs ./Zip/ZipConstants.cs \
    ./Zip/ZipStrings.cs ./Zip/WindowsNameTransform.cs \
    ./Zip/ZipEncryptionMethod.cs \
    ./Tar/TarInputStream.cs ./Tar/InvalidHeaderException.cs ./Tar/TarException.cs ./Tar/TarArchive.cs ./Tar/TarBuffer.cs \
    ./Tar/TarHeader.cs ./Tar/TarEntry.cs ./Tar/TarExtendedHeaderReader.cs ./Tar/TarOutputStream.cs \
    ./GZip/GzipInputStream.cs ./GZip/GZip.cs ./GZip/GZipException.cs ./GZip/GZipConstants.cs ./GZip/GzipOutputStream.cs \
    ./Encryption/ZipAESTransform.cs ./Encryption/ZipAESStream.cs ./Encryption/PkzipClassic.cs \
    ./Checksum/BZip2Crc.cs ./Checksum/Adler32.cs ./Checksum/IChecksum.cs ./Checksum/Crc32.cs \
    ./Checksum/CrcUtilities.cs \
    ./AssemblyInfo.cs \
    -define:NETFRAMEWORK -define:NET45 \
    -keyfile:../../assets/ICSharpCode.SharpZipLib.snk \
    -target:library -out:../../bin/ICSharpCode.SharpZipLib.dll
cd -

%install
mkdir -p %{buildroot}/%{_monogacdir} %{buildroot}/%{_libdir}/pkgconfig
gacutil -i bin/*.dll -f -package %{name} -root %{buildroot}/usr/lib

cat > %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc <<FINISH
prefix=/usr
exec_prefix=\${prefix}
libdir=\${exec_prefix}/lib

Name: sharpziplib
Description: C# Zip, GZip, Tar and BZip2 library for .NET
Version: %{version}
Libs: -r:\${libdir}/mono/sharpziplib/ICSharpCode.SharpZipLib.dll
FINISH

%check

%files
%license LICENSE.txt
%doc README.md
# usage of wildcards cause of weird dll name
%{_monogacdir}/*%{libname}
%{_monodir}/%{name}/*%{libname}.dll
%dir %{_monodir}/%{name}

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
