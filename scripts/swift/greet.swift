import Foundation

let name = CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : "friend"
print("Hello, \(name)! This greeting came from a Swift script running inside a Weave.")