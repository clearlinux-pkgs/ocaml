Name     : ocaml
Version  : 4.04.0
Release  : 1
URL      : http://caml.inria.fr/pub/distrib/ocaml-4.04/ocaml-4.04.0.tar.xz
Source0  : http://caml.inria.fr/pub/distrib/ocaml-4.04/ocaml-4.04.0.tar.xz
Patch1   : 0001-configure-Allow-user-defined-C-compiler-flags.patch
Summary  : programming language
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires : ocaml-bin
Requires : ocaml-lib
BuildRequires : util-linux

# temporarily manually add these until our rpm auto-generates these properly
Provides: ocaml(Arg)
Provides: ocaml(Array)
Provides: ocaml(Buffer)
Provides: ocaml(Bytes)
Provides: ocaml(CamlinternalFormatBasics)
Provides: ocaml(CamlinternalLazy)
Provides: ocaml(Char)
Provides: ocaml(Digest)
Provides: ocaml(Filename)
Provides: ocaml(Format)
Provides: ocaml(Hashtbl)
Provides: ocaml(Lazy)
Provides: ocaml(Lexing)
Provides: ocaml(List)
Provides: ocaml(Map)
Provides: ocaml(Pervasives)
Provides: ocaml(Printexc)
Provides: ocaml(Printf)
Provides: ocaml(Queue)
Provides: ocaml(runtime)
Provides: ocaml(Scanf)
Provides: ocaml(Set)
Provides: ocaml(String)
Provides: ocaml(Sys)
Provides: ocaml(Unix)

%package bin
License:        GPL-2.0 LGPL-2.1
Summary:        programming language
Group:          doc
Requires:       ocaml-lib

%description bin
programming language

%package lib
License:        GPL-2.0 LGPL-2.1
Summary:        programming language
Group:          doc
Provides:	ocaml(runtime) = %{version}

%description lib
programming language

%description
OCaml is an industrial strength programming language supporting functional,
imperative and object-oriented styles

%package doc
License:        GPL-2.0 LGPL-2.1
Summary:        programming language
Group:          doc

%description doc
programming language

%prep
%setup -q -n ocaml-4.04.0
%patch1 -p1

%build
export LANG=C
./configure -prefix /usr -libdir /usr/lib64/ocaml -mandir /usr/share/man -fPIC
make world opt opt.opt

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.cmt' -a -delete
find %{buildroot} -name '*.cmti' -a -delete
install -m0644 otherlibs/unix/libunix.a %{buildroot}/usr/lib64/ocaml/
install -m0644 otherlibs/unix/unix.a %{buildroot}/usr/lib64/ocaml/
install -m0644 stdlib/libasmrun.a %{buildroot}/usr/lib64/ocaml/
install -m0644 stdlib/libcamlrun.a %{buildroot}/usr/lib64/ocaml
install -m0644 stdlib/stdlib.a %{buildroot}/usr/lib64/ocaml/
install -m0755 tools/ocamlobjinfo %{buildroot}/usr/bin

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/ocaml/*

%files doc
%defattr(-,root,root,-)
/usr/share/man/*
